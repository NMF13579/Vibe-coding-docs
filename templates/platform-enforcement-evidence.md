# Platform Enforcement Evidence

Create one platform enforcement evidence record per protected branch.
dev and main must be verified separately.
Silent bypass is forbidden.
Silent admin bypass is forbidden.
Admin bypass must be disabled or explicitly documented with reason and record path.

This evidence record is not approval.
This evidence record does not authorize auto-merge.
This evidence record does not authorize automatic approval.
This evidence record only documents platform enforcement state.

## Evidence Details
- **Evidence ID**: 
- **Repository**: 
- **Branch**: 
- **Evidence date**: 
- **Human verifier**: 

## Platform State
- **Protected branch enabled**: [YES / NO]
- **Required status checks enabled**: [YES / NO]
- **Required check observed**: 
- **Expected required check**: 
- **Match**: [YES / NO]
- **Pull request review required**: [YES / NO]
- **Force-push allowed**: [YES / NO]
- **Branch deletion allowed**: [YES / NO]
- **Bypass permissions**: 
- **Bypass reason**: (mandatory if bypass permissions are non-empty)
- **Bypass record path**: (mandatory if bypass permissions are non-empty)
- **Admin bypass allowed**: [YES / NO]
- **Admin bypass reason**: (mandatory if Admin bypass allowed = YES)
- **Admin bypass record path**: (mandatory if Admin bypass allowed = YES)

## Evidence Source
- **Evidence source**: 
- **Screenshot / link / audit reference**: 

## Verification Result
- **Gaps found**: 

### Final platform enforcement status
Allowed statuses:
- PLATFORM_ENFORCED            = all required checks enabled, no gaps found
- PARTIAL_PLATFORM_ENFORCEMENT = some checks enabled, gaps documented
- NOT_ENFORCED                 = branch protection not enabled or required check not configured
- NEEDS_REVIEW                 = ambiguous or incomplete evidence

- **Final platform enforcement status**: 
