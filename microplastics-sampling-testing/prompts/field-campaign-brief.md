# Prompt — Field Campaign Brief

## Purpose

Generate a one-page, field-ready brief for a sampling campaign so the crew has gear, custody, contamination-control, and blank-handling nailed down before they leave.

## Prompt Template

```
Write a field campaign brief for the {campaign_name} microplastics survey.

Context:
- Sites & geometry: {site_list_with_station_geometry}
- Matrix: {water | sediment | biota | air}
- Gear / aperture: {net_mesh_or_filter_pore_and_size_class}
- Replicates per site: {n}
- Field-blank schedule: {per_site | per_day}
- Logistics window: {tide_flow_or_weather_window}, crew {n}

Produce:
1. Per-site task list (geometry, volume/tow, replicates, blank placement).
2. Gear & contamination-control checklist (glass/metal, cotton coats, covers).
3. Custody steps: seal IDs to pre-stage, who signs at collection.
4. Sample-volume floor to clear {target_relative_error} counting uncertainty.
5. Stop conditions (gear failure, weather, custody break) and the fallback.
```

## Expected Output

A printable brief: numbered per-site tasks, a tick-box gear/contamination checklist, the custody seal/sign procedure, the volume floor with its Poisson justification, and explicit stop/fallback rules. Should fit on one page and require no further interpretation in the field.
