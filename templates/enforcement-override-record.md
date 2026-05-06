# Enforcement Override Record

This override record is not automatic approval.
This override record does not authorize auto-merge.
This override record does not convert CI failure into PASS.
This override record does not prove platform enforcement.
This override record must be reviewed by a human owner.
Silent bypass is forbidden.
Open-ended override is forbidden.

## Record Fields

- Override ID:
- Date:
- Repository:
- Branch:
- Related PR / commit:
- Related check:
- AgentOS result:
- Blocking result present: YES / NO
- WARN present: YES / NO
- Override type:
- Override applies to: WARN / FAIL / ERROR / NOT_RUN / INCOMPLETE / PLATFORM_LIMITATION / ADMIN_BYPASS
- Override reason:
- Risk accepted:
- Evidence links / artifacts:
- Human reviewer:
- Owner approval:
- Override expiry:
- One-time scope:
- Bypass used: YES / NO
- Bypass type:
- Admin bypass used: YES / NO
- Follow-up required: YES / NO
- Follow-up action:
- Final decision: APPROVED_WITH_OVERRIDE / BLOCKED / NEEDS_REVIEW
- Final statement:

## Allowed Override Types

- WARN_REVIEW
- PLATFORM_LIMITATION
- EMERGENCY_EXCEPTION
- ADMIN_BYPASS_RECORD
- OWNER_OVERRIDE

## Allowed Final Decisions

- APPROVED_WITH_OVERRIDE
- BLOCKED
- NEEDS_REVIEW

## Required Rules

If Blocking result present = YES, Owner approval is mandatory.
If Admin bypass used = YES, Bypass type and evidence links are mandatory.
If Final decision = APPROVED_WITH_OVERRIDE, Override expiry or One-time scope is mandatory.
If Follow-up required = YES, Follow-up action is mandatory.

## Notes

- This template is for a human-reviewed record.
- This template does not approve any change by itself.
- This template does not prove platform enforcement by itself.
- This template must be filled out before any override is treated as documented.
