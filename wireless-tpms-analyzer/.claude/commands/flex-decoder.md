# Flex Decoder

Generate an rtl_433 flex decoder configuration for an unrecognized or custom TPMS sensor.

## Usage

Provide your protocol analysis results from `/protocol-map`, or give me the key parameters directly:

**Required:**
- Modulation type: `OOK_PWM`, `OOK_PPM`, `OOK_MC_ZEROBIT`, `FSK_PCM`, or `FSK_MC_ZEROBIT`
- Short pulse width (µs)
- Long pulse width (µs) — for PWM; or bit period for PCM
- Reset limit (µs) — gap after which a new packet starts
- Total packet bits

**Optional but helpful:**
- Preamble bit pattern (e.g., `aa aa aa 2d d4`)
- Field layout (bit offsets and widths)
- Checksum type and parameters

## Output format

I'll generate a complete rtl_433 flex decoder config like:

```
decoder
  n=My_Sensor_Name,
  m=OOK_PWM,
  s=200,
  l=400,
  r=8000,
  bits>=64,
  get=@0:{32}:id,
  get=@32:{8}:pressure_raw,
  get=@40:{8}:temperature_raw,
  get=@48:{8}:flags,
  get=@56:{8}:checksum
```

And the command to test it:
```bash
rtl_433 -f 315M -X 'n=My_Sensor,m=OOK_PWM,s=200,l=400,r=8000,bits>=64'
```

## Submitting to rtl_433

If the decoder works reliably, I'll help you format a pull request to the rtl_433 repository including:
- C decoder implementation outline
- Sample capture file reference
- Manufacturer/FCC documentation links
