# Portfolio — Legacy Django Project

This repository is retained as a **historical engineering project**. It is not the current engineering portfolio and should not be treated as an actively maintained production application.

## What it contains

The project is a Django 4.2-era multi-app application containing:

- `portfolio/` — Django project configuration
- `blog/` — blog functionality
- `jobs/` — jobs-related functionality
- `agenda/` — agenda/scheduling experiments
- `rota/` — rota/scheduling experiments
- `templates/` and `static/` — server-rendered UI assets

The repository is useful as a record of earlier Django/full-stack work, but newer product repositories should be used for active development.

## Status

**Lifecycle:** archive / historical reference

**Planned repository name:** `portfolio-legacy-django`

No feature development is planned here. If material from this repository is reused, migrate the specific idea or implementation into an actively maintained repository rather than reviving this codebase wholesale.

## Local configuration

The current tree no longer commits reusable local credentials. If you run the project locally, provide at least:

```bash
export DJANGO_SECRET_KEY='replace-for-local-use'
export POSTGRES_PASSWORD='replace-for-local-use'
```

The remaining settings are development-oriented and are **not production hardened**. `DEBUG` is enabled in the historical settings module.

## Security note

Older Git history contained development-only credential literals. They appeared to be local scaffold values rather than production secrets. If either value was ever reused in a deployed environment, rotate the corresponding credential/key before relying on that environment.

## Archive policy

This repository is being preserved for provenance and learning value. Archiving it on GitHub is intentional and does not imply that the code reflects current engineering standards.
