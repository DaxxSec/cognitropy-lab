# Forecast Report Template

Use this shape when assembling a stakeholder-facing forecast report. The release bundle's `cover-note.md` should follow this structure.

---

## Headline

- **Forecast:** GDP {{convention}} for {{target_quarter}}: **{{point}}** (95% band [{{lower}}, {{upper}}])
- **Change vs. prior published forecast:** {{delta}} ({{signed_pct}})
- **Vintage cutoff:** {{cutoff_date}}

## Methodology

- **Model class:** {{class}} ({{key_hyperparameters}})
- **Training window:** {{train_start}} through {{train_end}}
- **Indicator panel:** {{n_series}} series across labour, activity, surveys, and trade.
- **Real-time discipline:** all inputs are sealed vintages with `retrieved_utc <= cutoff_date`.

## Drivers

| Indicator | Contribution to forecast change |
|-----------|-------------------------------|
| {{indicator_1}} | {{contribution_1}} |
| {{indicator_2}} | {{contribution_2}} |
| {{indicator_3}} | {{contribution_3}} |
| {{indicator_4}} | {{contribution_4}} |
| {{indicator_5}} | {{contribution_5}} |

## Risks and Asymmetries

- {{risk_1}}
- {{risk_2}}
- {{risk_3}}

## Comparison with Consensus / External Nowcasts (informational)

| Source | Value | Note |
|--------|-------|------|
| GDPNow (Atlanta Fed) | {{gdpnow}} | as of {{gdpnow_date}} |
| NY Fed Nowcast | {{nyfed}} | as of {{nyfed_date}} |
| SPF (Philadelphia Fed) | {{spf}} | survey closes {{spf_date}} |

## Disclosures

- **Methodology:** the model class, training window, and vintage cutoff above.
- **Judgmental adjustments:** {{none|description}}
- **Conflict of interest:** {{firm_disclosure_block}}
- **Embargo respected:** all input series cleared embargo before this report's timestamp.

## Reproducibility Footer

- **Release bundle:** `outputs/forecasts/release__{{date}}/`
- **Manifest hash:** {{manifest_sha256}}
- **Signed by:** {{signing_fingerprint}}
- **Code commit:** {{git_sha}}

A reader holding the release bundle and this report can verify the headline number against the bundled manifest.
