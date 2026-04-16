# Generate SBOM

Produce a Software Bill of Materials from project dependency manifests.

## Instructions
1. Ask the user for the target format: CycloneDX 1.5 (default) or SPDX 2.3
2. Collect all dependency manifests from the project
3. Parse direct and transitive dependencies with version information
4. Resolve package URLs (PURLs) for each component
5. Include supplier information where determinable
6. Add license information for each component
7. Generate the SBOM in the requested format
8. Validate against NTIA minimum elements
9. Save to `outputs/` with appropriate extension (.json or .xml)

## Validation Checklist (NTIA Minimum Elements)
- [ ] Supplier name for each component
- [ ] Component name
- [ ] Component version
- [ ] Unique identifier (PURL)
- [ ] Dependency relationships mapped
- [ ] SBOM author identified
- [ ] Timestamp included
