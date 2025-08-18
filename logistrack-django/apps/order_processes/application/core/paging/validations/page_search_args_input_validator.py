from typing import Optional, List
from pydantic import BaseModel, field_validator, model_validator
from apps.order_processes.application.core.paging.models.page_search_args_input import SortingOption, FilterOption


class PageSearchArgsInputModel(BaseModel):
    page_index: int = 0
    page_size: int = 20
    sorting_options: Optional[List[SortingOption]] = None
    filtering_options: Optional[List[FilterOption]] = None
    paging_strategy: str = "default"

    @field_validator("page_index", mode="before")
    @classmethod
    def page_index_must_be_non_negative(cls, v):
        if v < 0:
            raise ValueError("Page index must be greater than or equal to 0")
        return v

    @field_validator("page_size", mode="before")
    @classmethod
    def page_size_must_be_valid(cls, v):
        if not (1 <= v <= 100):
            raise ValueError("Page size must be between 1 and 100")
        return v

    @model_validator(mode="before")
    @classmethod
    def validate_sorting_filtering_strategy(cls, values):
        sorting_options = values.get("sorting_options") or []
        filtering_options = values.get("filtering_options") or []

        # Validate sorting options
        for s in sorting_options:
            if not s.field.strip():
                raise ValueError("Sorting field cannot be empty")
            if s.direction not in ("asc", "desc"):
                raise ValueError(f"Sorting direction must be 'asc' or 'desc', got '{s.direction}'")

        # Validate filtering options
        for f in filtering_options:
            if not f.field.strip():
                raise ValueError("Filter field cannot be empty")
            if f.value is None or str(f.value).strip() == "":
                raise ValueError("Filter value cannot be empty")

        # Validate paging strategy
        allowed_strategies = ["default", "cursor", "keyset"]
        if values.get("paging_strategy") not in allowed_strategies:
            raise ValueError(f"Paging strategy must be one of {allowed_strategies}")

        return values