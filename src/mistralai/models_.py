"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from mistralai import models, utils
from mistralai._hooks import HookContext
from mistralai.types import OptionalNullable, SDKError, UNSET
from mistralai.utils import get_security_from_env
from typing import Any, Optional

class Models(BaseSDK):
    r"""Model Management API"""
    
    
    def list(
        self, *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ModelList]:
        r"""List Models

        List all models available to the user.

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
        req = self.build_request(
            method="GET",
            path="/v1/models",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
            hook_ctx=HookContext(operation_id="list_models_v1_models_get", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ModelList])
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def list_async(
        self, *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ModelList]:
        r"""List Models

        List all models available to the user.

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
        req = self.build_request(
            method="GET",
            path="/v1/models",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
            hook_ctx=HookContext(operation_id="list_models_v1_models_get", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ModelList])
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def retrieve(
        self, *,
        model_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ModelCard]:
        r"""Retrieve Model

        Retrieve a model information.

        :param model_id: The ID of the model to retrieve.
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
        
        request = models.RetrieveModelV1ModelsModelIDGetRequest(
            model_id=model_id,
        )
        
        req = self.build_request(
            method="GET",
            path="/v1/models/{model_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
            hook_ctx=HookContext(operation_id="retrieve_model_v1_models__model_id__get", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ModelCard])
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def retrieve_async(
        self, *,
        model_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ModelCard]:
        r"""Retrieve Model

        Retrieve a model information.

        :param model_id: The ID of the model to retrieve.
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
        
        request = models.RetrieveModelV1ModelsModelIDGetRequest(
            model_id=model_id,
        )
        
        req = self.build_request(
            method="GET",
            path="/v1/models/{model_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
            hook_ctx=HookContext(operation_id="retrieve_model_v1_models__model_id__get", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ModelCard])
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def delete(
        self, *,
        model_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.DeleteModelOut]:
        r"""Delete Model

        Delete a fine-tuned model.

        :param model_id: The ID of the model to delete.
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
        
        request = models.DeleteModelV1ModelsModelIDDeleteRequest(
            model_id=model_id,
        )
        
        req = self.build_request(
            method="DELETE",
            path="/v1/models/{model_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
            hook_ctx=HookContext(operation_id="delete_model_v1_models__model_id__delete", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DeleteModelOut])
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def delete_async(
        self, *,
        model_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.DeleteModelOut]:
        r"""Delete Model

        Delete a fine-tuned model.

        :param model_id: The ID of the model to delete.
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
        
        request = models.DeleteModelV1ModelsModelIDDeleteRequest(
            model_id=model_id,
        )
        
        req = self.build_request(
            method="DELETE",
            path="/v1/models/{model_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
            hook_ctx=HookContext(operation_id="delete_model_v1_models__model_id__delete", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DeleteModelOut])
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def update(
        self, *,
        model_id: str,
        name: OptionalNullable[str] = UNSET,
        description: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.FTModelOut]:
        r"""Update Fine Tuned Model

        Update a model name or description.

        :param model_id: The ID of the model to update.
        :param name: 
        :param description: 
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
        
        request = models.JobsAPIRoutesFineTuningUpdateFineTunedModelRequest(
            model_id=model_id,
            update_ft_model_in=models.UpdateFTModelIn(
                name=name,
                description=description,
            ),
        )
        
        req = self.build_request(
            method="PATCH",
            path="/v1/fine_tuning/models/{model_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.update_ft_model_in, False, False, "json", models.UpdateFTModelIn),
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
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_update_fine_tuned_model", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.FTModelOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def update_async(
        self, *,
        model_id: str,
        name: OptionalNullable[str] = UNSET,
        description: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.FTModelOut]:
        r"""Update Fine Tuned Model

        Update a model name or description.

        :param model_id: The ID of the model to update.
        :param name: 
        :param description: 
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
        
        request = models.JobsAPIRoutesFineTuningUpdateFineTunedModelRequest(
            model_id=model_id,
            update_ft_model_in=models.UpdateFTModelIn(
                name=name,
                description=description,
            ),
        )
        
        req = self.build_request(
            method="PATCH",
            path="/v1/fine_tuning/models/{model_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.update_ft_model_in, False, False, "json", models.UpdateFTModelIn),
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
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_update_fine_tuned_model", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.FTModelOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def archive(
        self, *,
        model_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ArchiveFTModelOut]:
        r"""Archive Fine Tuned Model

        Archive a fine-tuned model.

        :param model_id: The ID of the model to archive.
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
        
        request = models.JobsAPIRoutesFineTuningArchiveFineTunedModelRequest(
            model_id=model_id,
        )
        
        req = self.build_request(
            method="POST",
            path="/v1/fine_tuning/models/{model_id}/archive",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_archive_fine_tuned_model", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ArchiveFTModelOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def archive_async(
        self, *,
        model_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ArchiveFTModelOut]:
        r"""Archive Fine Tuned Model

        Archive a fine-tuned model.

        :param model_id: The ID of the model to archive.
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
        
        request = models.JobsAPIRoutesFineTuningArchiveFineTunedModelRequest(
            model_id=model_id,
        )
        
        req = self.build_request(
            method="POST",
            path="/v1/fine_tuning/models/{model_id}/archive",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_archive_fine_tuned_model", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ArchiveFTModelOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def unarchive(
        self, *,
        model_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.UnarchiveFTModelOut]:
        r"""Unarchive Fine Tuned Model

        Un-archive a fine-tuned model.

        :param model_id: The ID of the model to unarchive.
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
        
        request = models.JobsAPIRoutesFineTuningUnarchiveFineTunedModelRequest(
            model_id=model_id,
        )
        
        req = self.build_request(
            method="DELETE",
            path="/v1/fine_tuning/models/{model_id}/archive",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_unarchive_fine_tuned_model", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.UnarchiveFTModelOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def unarchive_async(
        self, *,
        model_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.UnarchiveFTModelOut]:
        r"""Unarchive Fine Tuned Model

        Un-archive a fine-tuned model.

        :param model_id: The ID of the model to unarchive.
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
        
        request = models.JobsAPIRoutesFineTuningUnarchiveFineTunedModelRequest(
            model_id=model_id,
        )
        
        req = self.build_request(
            method="DELETE",
            path="/v1/fine_tuning/models/{model_id}/archive",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
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
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_unarchive_fine_tuned_model", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.UnarchiveFTModelOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
