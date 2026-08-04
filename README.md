# Reasoning Effort

Adds a reasoning-effort selector after Agent Zero's preset and agent-profile controls.

The plugin asks its authenticated local API for the active chat model's capabilities. The API reads LiteLLM's bundled model registry first, then falls back to live model metadata from Agent Zero API, Venice, and OpenRouter. Provider requests use Agent Zero's server-side configuration and are cached for 15 minutes. Provider-specific labels remain separate from the canonical values passed to LiteLLM.

You can enter a custom value when neither LiteLLM nor the provider publishes a list. Models explicitly marked unsupported by the provider show **Unsupported** instead. A selection applies only to the current chat and model; choosing **Preset / provider default** removes the override.

## OpenAI-compatible provider forwarding

LiteLLM may drop unknown top-level parameters when Agent Zero's `drop_params`
default is enabled. This matters for providers such as Z.AI when LiteLLM does
not advertise the model's reasoning-effort vocabulary (for example,
`zai_coding/glm-5.2`).

The plugin therefore forwards a selected custom effort through both
`reasoning_effort` and `extra_body.reasoning_effort`. The latter preserves the
provider-specific value through LiteLLM's OpenAI-compatible transport. Provider
configuration may also declare a custom `reasoning_efforts` vocabulary.

## Install

Place this directory at `usr/plugins/a0_reasoning_effort` in Agent Zero, then reload the WebUI. No additional dependencies are required.

## Check

From the Agent Zero root:

```bash
python usr/plugins/a0_reasoning_effort/helpers/reasoning_effort.py
```
