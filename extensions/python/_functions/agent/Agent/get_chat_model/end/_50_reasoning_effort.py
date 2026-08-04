from helpers.extension import Extension
from usr.plugins.a0_reasoning_effort.helpers.reasoning_effort import get_override


class ReasoningEffortOverride(Extension):
    def execute(self, data: dict = {}, **kwargs):
        model = data.get("result")
        effort = get_override(self.agent) if self.agent and model else ""
        if effort and isinstance(getattr(model, "kwargs", None), dict):
            model.kwargs["reasoning_effort"] = effort
            # Custom OpenAI-compatible providers (z.ai and the like) drop unknown
            # top-level params under drop_params, so mirror the effort into
            # extra_body -- litellm forwards it verbatim, and it overrides any
            # provider-level default extra_body.reasoning_effort.
            extra_body = dict(model.kwargs.get("extra_body") or {})
            extra_body["reasoning_effort"] = effort
            model.kwargs["extra_body"] = extra_body
