"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from mistralai import models, utils
from mistralai._hooks import HookContext
from mistralai.types import OptionalNullable, SDKError, UNSET
from mistralai.utils import get_security_from_env
from typing import Any, Optional, Union

class Embeddings(BaseSDK):
    r"""Embeddings API."""
    
    
    def create(
        self, *,
        inputs: Union[models.Inputs, models.InputsTypedDict],
        model: str,
        encoding_format: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.EmbeddingResponse]:
        r"""Embeddings

        Embeddings

        :param inputs: Text to embed.
        :param model: ID of the model to use.
        :param encoding_format: The format to return the embeddings in.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.EmbeddingRequest(
            inputs=inputs,
            model=model,
            encoding_format=encoding_format,
        )
        
        req = self.build_request(
            method="POST",
            path="/v1/embeddings",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.EmbeddingRequest),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="embeddings_v1_embeddings_post", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.EmbeddingResponse])
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def create_async(
        self, *,
        inputs: Union[models.Inputs, models.InputsTypedDict],
        model: str,
        encoding_format: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.EmbeddingResponse]:
        r"""Embeddings

        Embeddings

        :param inputs: Text to embed.
        :param model: ID of the model to use.
        :param encoding_format: The format to return the embeddings in.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.EmbeddingRequest(
            inputs=inputs,
            model=model,
            encoding_format=encoding_format,
        )
        
        req = self.build_request(
            method="POST",
            path="/v1/embeddings",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.EmbeddingRequest),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="embeddings_v1_embeddings_post", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.EmbeddingResponse])
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
