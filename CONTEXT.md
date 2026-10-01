# CouncilDataProject/cdp-backend context
> refreshed 2026-10-01 | upstream default: main @ fda26250d66a076a05772dda2f9a109d34ac6a03

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
- dedupe (2026-09-30): no upstream issue or PR mentions `get_media_type`; the only `media type` hit is #235/#138 (hosting/resource-copy), unrelated. PR #247 (time_duration_is_valid regex) was an automated bot PR self-closed as incorrect, not maintainer-engaged

## Gap ledger (dedupe — READ FIRST, never re-pick)
one bullet per attempt:
- `2026-09-08` self-found trivial-errors cleanup (6 fixes, 6 files: CONTRIBUTING dead link, satifactory typo, get-cdp-infrastructure-stack stale command, existance/relavent/it's typos) — pr-opened https://github.com/olitreadwell/cdp-backend/pull/3 — fork CI red on main too (env: mypy/yaml-stubs py3.11, av wheel build); locally verified 66 tests pass
- `2026-09-09` EXTENDED PR #3 (same theme, not a new PR): added 5 more typo fixes across 4 files (infered->inferred x2 in pipeline_config.py user-facing error; retrive->retrieve file_utils.py; commited->committed speaker_labels.py; cant->can't + coonvert->convert event_gather_pipeline.py) — pr-updated https://github.com/olitreadwell/cdp-backend/pull/3 — combined 10 files, 11/11, head bb73927a, mergeable=True; skipped valid variants (unsecure, re-use) and test-fixture strings (doesnt://matter, doesnt.matter)
- `2026-09-24` self-found bug fix find_proper_resize_ratio (returns max of scale factors so non-16:9 thumbnails stay oversized) — pr-opened https://github.com/olitreadwell/cdp-backend/pull/4 — fork CI red on main too (env: mypy/yaml-stubs, av wheel build); locally verified new test passes (6 cases) + ruff/black clean
- `2026-09-24` self-found bug fix convert_gcs_json_url_to_gsutil_form (percent-encoded GCS object names not decoded -> wrong gsutil URI -> resource_exists reports valid resources missing) — pr-opened https://github.com/olitreadwell/cdp-backend/pull/5 — 3 new parametrized cases fail pre-fix, pass post-fix; ruff+black pass; mypy/av-wheel are pre-existing fork-main env failures
- `2026-09-24` self-found bug fix resource_copy default dst filename kept query string/fragment (uri.split("/")[-1]) -> wrote files literally named example_video.mp4?token=abc&alt=media; new _uri_derived_filename() strips ?.../#..., used in no-dst + directory-dst branches; 4 parametrized cases pass — pr-opened https://github.com/olitreadwell/cdp-backend/pull/6 — black+py_compile clean; mypy/av-wheel pre-existing fork-main env failures

- `2026-09-30` self-found bug fix get_media_type (`uri.split(".")[-1]` corrupts the suffix, so query strings/fragments/uppercase extensions never match the IANA name column and the function returns None) — pr-opened https://github.com/olitreadwell/cdp-backend/pull/7 — 5 new parametrized cases fail pre-fix, pass post-fix; black+ruff+py_compile clean; fork CI red on main too (env: mypy/yaml-stubs py3.11, av wheel build)
- `2026-10-01` self-found trivial-errors cleanup, pass 2 (8 fixes, 7 files: README CI badge 404 -> actions/workflows/ci.yml badge path; CONTRIBUTING Just Commands list `test` -> `test-functions`+`test-library`; gcloud-functions README `--target hello_http` -> `generate_clip`; comment typos divison/accesible x3/guarentee) — pr-opened https://github.com/olitreadwell/cdp-backend/pull/8 — locally: 8 tests pass in test_pipeline_config.py, black 22.6.0 + ruff 0.0.216 clean, py_compile clean; fork CI red on main too (mypy/yaml-stubs py3.11, av wheel build)

## Mined gaps (discovered, not yet attempted)
one bullet per candidate:
- `2026-09-08` CONTRIBUTING.md links to deleted `.github/workflows/build-main.yml` (removed in #201, 2022); current file is `.github/workflows/ci.yml` — stale/broken link
- `2026-09-08` docs/event_gather_pipeline.md typo "satifactory" -> "satisfactory"
- `2026-09-08` dev-infrastructure/README.md stale command "get-cdp-infrastructure-stack" -> actual console script "get_cdp_infrastructure_stack"
- `2026-09-08` cdp_backend/database/validators.py docstring typo "existance" -> "existence"
- `2026-09-08` cdp_backend/pipeline/ingestion_models.py docstring typo "relavent" -> "relevant"
- `2026-09-08` cdp_backend/pipeline/transcript_model.py docstring "it's respective transcript" -> "its respective transcript"
- `2026-09-09` cdp_backend/pipeline/pipeline_config.py error message "infered" -> "inferred" (2x) — done in PR #3
- `2026-09-24` cdp_backend/utils/file_utils.py find_proper_resize_ratio chooses max(height_ratio, width_ratio), so a portrait or wide source can still exceed MAX_THUMBNAIL_WIDTH/MAX_THUMBNAIL_HEIGHT after resize — should use min — done in PR #4
- `2026-09-24` cdp_backend/utils/string_utils.py convert_gcs_json_url_to_gsutil_form leaves object name percent-encoded (%20 space, %2F /, parens); gsutil needs decoded name; fix urllib.parse.unquote — done in PR #5
- `2026-09-09` cdp_backend/utils/file_utils.py docstring "retrive" -> "retrieve" — done in PR #3
- `2026-09-09` cdp_backend/annotation/speaker_labels.py docstring "commited" -> "committed" — done in PR #3
- `2026-09-09` cdp_backend/pipeline/event_gather_pipeline.py comment "cant"/"coonvert" -> "can't"/"convert" — done in PR #3
- `2026-09-30` cdp_backend/utils/file_utils.py get_media_type returns None for URIs with a query string/fragment or uppercase extension (suffix taken from `uri.split(".")[-1]`) — done in PR #7
- `2026-09-30` cdp_backend/database/models.py generate_router_string raises IndexError (`spaces_replaced[-1]`) for a name that cleans to empty (e.g. "李雷"), instead of a clear error — status: proposed
- `2026-09-30` cdp_backend/pipeline/event_gather_pipeline.py convert_video_and_handle_host can leave `hosted_video_media_url` unbound (UnboundLocalError) when a secure video URI fails resource_exists and its www variant does not exist either — status: proposed
- `2026-10-01` README.md CI status badge URL `workflows/CI/badge.svg` 404s (verified); use `actions/workflows/ci.yml/badge.svg` — done in PR #8
- `2026-10-01` CONTRIBUTING.md "Just Commands" list documents a `test` recipe that does not exist in the Justfile; actual recipes are `test-library` + `test-functions` — done in PR #8
- `2026-10-01` cdp_backend/infrastructure/gcloud-functions/README.md debug command uses `--target hello_http` but the function is `generate_clip` — done in PR #8
- `2026-10-01` comment typos: generate_event_index_pipeline.py "divison"; test_event_gather_pipeline.py/test_event_index_pipeline.py/test_pipeline_config.py "accesible"; test_event_gather_pipeline.py "guarentee" — done in PR #8
