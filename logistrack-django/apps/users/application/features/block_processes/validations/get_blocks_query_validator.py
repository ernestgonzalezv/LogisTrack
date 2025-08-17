from apps.users.application.features.block_processes.queries.get_blocks_query import GetOrdersQuery

def validate_get_blocks_query(query: GetOrdersQuery):
    """
    Validates that the orders query contains the required data.
    """
    if not query:
        raise ValueError("Query cannot be None")
    if not query.page_args:
        raise ValueError("PageSearchArgs is required")
    if query.page_args.page_index < 0:
        raise ValueError("page_index cannot be negative")
    if query.page_args.page_size <= 0:
        raise ValueError("page_size must be greater than 0")
