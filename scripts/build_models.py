"""One-shot model generator: inspectdb + clean + split."""
import os, re, subprocess, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SCHEMAS = {"afya": "afya,public", "audit": "audit,public", "research": "research,public"}

MAPPING = {
    "Users":"accounts","Roles":"accounts","Permissions":"accounts","UserRoles":"accounts",
    "RolePermissions":"accounts","Organizations":"accounts","OrgMemberships":"accounts",
    "LoginSessions":"accounts","OtpCodes":"accounts",
    "AdminAreas":"core","Farmers":"core","CropTypes":"core","Farms":"core",
    "FarmActivities":"core","HarvestRecords":"core",
    "Questionnaires":"wellbeing","QuestionnaireVersions":"wellbeing","Questions":"wellbeing",
    "QuestionOptions":"wellbeing","Checkins":"wellbeing","CheckinResponses":"wellbeing",
    "StressorTypes":"wellbeing","StressorLogs":"wellbeing","ScoringRules":"wellbeing",
    "DimensionScores":"wellbeing","CheckinAssessments":"wellbeing","AnalysisRules":"wellbeing",
    "Counselors":"support","Referrals":"support","PeerGroups":"support","GroupMembers":"support",
    "Subscriptions":"support","Payments":"support","Notifications":"support",
    "Institutions":"research","ResearchProjects":"research","ProjectMembers":"research",
    "EthicsApprovals":"research","Consents":"research","DataAccessRequests":"research",
    "Datasets":"research","DatasetExports":"research","ResearchPidMap":"research",
    "VAnonymizedCheckins":"research","VAnonymizedDimensionScores":"research",
    "AuditLogs":"auditlayer","DataAccessLogs":"auditlayer","LoginAttempts":"auditlayer",
    "SecurityEvents":"auditlayer","RecordHistory":"auditlayer","ApiRequestLogs":"auditlayer",
    "ConsentHistory":"auditlayer",
}
SKIP = {"DjangoMigrations","AuthGroup","AuthPermission","AuthUser","DjangoSession","DjangoAdminLog"}

def run_inspectdb(sp):
    env = os.environ.copy(); env["DB_SEARCH_PATH"] = sp
    r = subprocess.run([sys.executable,"manage.py","inspectdb"], cwd=str(BASE), env=env,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError(r.stderr)
    return r.stdout

def split_classes(t):
    pat = re.compile(r"^class (\w+)\(.*?\):.*?(?=^class |\Z)", re.M | re.S)
    return {m.group(1): m.group(0) for m in pat.finditer(t)}

def clean_block(src, schema):
    def repl(m):
        tb = m.group(1)
        return m.group(0) if '"' in tb else f'db_table = \'{schema}"."{tb}\''
    src = re.sub(r"db_table = '([^']+)'", repl, src)
    if "class Meta:" in src and "managed = False" not in src:
        src = src.replace("class Meta:\n", "class Meta:\n        managed = False\n", 1)
    return src

def qualify_fks(text):
    for cls, app in MAPPING.items():
        for t in ("ForeignKey","OneToOneField"):
            text = re.sub(rf"\b{t}\(\s*{cls}\b",  f"{t}('{app}.{cls}'", text)
            text = re.sub(rf"\b{t}\(\s*'{cls}'",  f"{t}('{app}.{cls}'", text)
            text = re.sub(rf'\b{t}\(\s*"{cls}"',  f"{t}('{app}.{cls}'", text)
    return text

def main():
    collected = {}
    for schema, sp in SCHEMAS.items():
        print(f"[{schema}] inspectdb ...")
        try:
            raw = run_inspectdb(sp)
        except RuntimeError as e:
            print(f"[{schema}] FAILED: {e}"); continue
        cls = split_classes(raw)
        print(f"[{schema}] {len(cls)} classes found")
        for name, src in cls.items():
            if name not in SKIP:
                collected[name] = (schema, src)
    if not collected:
        print("No classes collected"); return 1
    by_app, unmapped = {}, []
    for name, (schema, src) in collected.items():
        app = MAPPING.get(name)
        if not app:
            unmapped.append(name); continue
        by_app.setdefault(app, []).append(clean_block(src, schema))
    print()
    for app in sorted(by_app):
        target = BASE / app / "models.py"
        if not target.parent.exists():
            print(f"  SKIP: {app}/ not found"); continue
        hdr = (f'"""\n{app.capitalize()} models — generated from live DB.\n"""\n'
               f'import uuid\nfrom django.db import models\n\n\n')
        body = qualify_fks("\n\n".join(by_app[app]))
        target.write_text(hdr + body, encoding="utf-8", newline="\n")
        print(f"  WROTE {app}/models.py  ({len(by_app[app])} classes, {target.stat().st_size} bytes)")
    if unmapped:
        print(f"\n  UNMAPPED: {', '.join(sorted(unmapped))}")
    print(f"\nDone. {sum(len(v) for v in by_app.values())} models across {len(by_app)} apps.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
