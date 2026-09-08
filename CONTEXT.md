# CouncilDataProject/cdp-backend context
> refreshed 2026-09-08 | upstream default: main @ fda26250d66a076a05772dda2f9a109d34ac6a03

## Identity & policies
- upstream: CouncilDataProject/cdp-backend, default branch main, primary language Python, English-first: yes (all docs in English)
- CLA/DCO: none found in CONTRIBUTING / .github
- AI-assisted PR policy: unstated (no AI disclosure requirement found)
- signed commits required: no (no branch protection on main; API returns 404)
- PR template: .github/PULL_REQUEST_TEMPLATE.md (fill verbatim; sections: Link to Relevant Issue, Description of Changes)
- external tracker: github

## Conventions (verified from merged PRs)
- branch naming: `{type}/{kebab-description}` e.g. bugfix/unique-temp-filenames, chore/..., feature/..., docs/...
- commit style: single detailed commit message
- test command: `just test` (test-library + test-functions); lint via `pre-commit run --all-files` (just lint)
- CI checks that gate merge: GitHub Actions ci.yml (CI: tests + lint + build) and docs.yml

## Maintainer picture
- primary maintainer: evamaxfield (Eva Maxfield Brown)
- repo largely dormant since ~2024 (last default-branch commit 2024-03-01; pushed_at 2026-02-11 is non-main activity)

## Issue-area health
- repo inactive for new development; low volume of open issues/PRs
- fork PRs should be tiny, low-risk, easy-to-scan (consistent with trivial/minor-fix pass)

## Gap ledger (dedupe — READ FIRST, never re-pick)
one bullet per attempt:
one bullet per attempt:
- `2026-09-08` self-found trivial-errors cleanup (6 fixes, 6 files: CONTRIBUTING dead link, satifactory typo, get-cdp-infrastructure-stack stale command, existance/relavent/it's typos) — pr-opened https://github.com/olitreadwell/cdp-backend/pull/3 — fork CI red on main too (env: mypy/yaml-stubs py3.11, av wheel build); locally verified 66 tests pass

## Mined gaps (discovered, not yet attempted)
one bullet per candidate:
- `2026-09-08` CONTRIBUTING.md links to deleted `.github/workflows/build-main.yml` (removed in #201, 2022); current file is `.github/workflows/ci.yml` — stale/broken link
- `2026-09-08` docs/event_gather_pipeline.md typo "satifactory" -> "satisfactory"
- `2026-09-08` dev-infrastructure/README.md stale command "get-cdp-infrastructure-stack" -> actual console script "get_cdp_infrastructure_stack"
- `2026-09-08` cdp_backend/database/validators.py docstring typo "existance" -> "existence"
- `2026-09-08` cdp_backend/pipeline/ingestion_models.py docstring typo "relavent" -> "relevant"
- `2026-09-08` cdp_backend/pipeline/transcript_model.py docstring "it's respective transcript" -> "its respective transcript"
