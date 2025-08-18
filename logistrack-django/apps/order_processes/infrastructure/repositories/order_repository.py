from django.db.models import Prefetch
from apps.order_processes.application.core.paging.models.page_search_args import PageSearchArgs
from apps.order_processes.application.core.paging.models.query_result import QueryResult
from apps.order_processes.domain.repositories.order_repository import IOrderRepository
from apps.order_processes.infrastructure.map_profiles.order_mapper import map_orders
from apps.order_processes.infrastructure.orm_models.models import (
    Order as OrderModel,
    BlockOrder,
    OrderProduct as OrderProductModel,
    Incidence as IncidenceModel,
)

class OrderRepository(IOrderRepository):

    def get_orders_by_stage(
        self,
        page_args: PageSearchArgs,
    ) -> QueryResult:

        print(f"🟢 Starting get_orders_by_stage | page_index={page_args.page_index}, page_size={page_args.page_size}")

        try:
            # Base queryset
            qs = OrderModel.objects.select_related(
                "pyme",
                "distribution_center"
            ).prefetch_related(
                Prefetch(
                    "orderproduct_set",
                    queryset=OrderProductModel.objects.select_related("product")
                ),
                Prefetch(
                    "incidence_set",
                    queryset=IncidenceModel.objects.all()
                ),
                Prefetch(
                    "blockorder_set",
                    queryset=BlockOrder.objects.select_related("block__driver")
                )
            )

            # Aplicar filtros
            if page_args.filtering_options:
                for f in page_args.filtering_options:
                    field = f.field
                    value = f.value
                    if not field or value is None:
                        continue

                    if field == "pyme_name":
                        qs = qs.filter(pyme__name__icontains=value)
                        print(f"⚡ Filter: pyme_name contains {value.lower()}")
                    elif field == "distribution_center_name":
                        qs = qs.filter(distribution_center__name__icontains=value)
                        print(f"⚡ Filter: distribution_center_name contains {value}")
                    elif field == "status":
                        qs = qs.filter(status=value)
                        print(f"⚡ Filter: status = {value}")
                    elif field == "driver_name":
                        qs = qs.filter(blockorder__block__driver__name__icontains=value)
                        print(f"⚡ Filter: driver name contains {value}")
                    elif field == "product_sku":
                        qs = qs.filter(orderproduct__product__sku__icontains=value)
                        print(f"⚡ Filter: product SKU contains {value}")
                    elif field == "dispatch_date_start":
                        qs = qs.filter(dispatch_date__gte=value)
                        print(f"⚡ Filter: dispatch_date >= {value}")
                    elif field == "dispatch_date_end":
                        qs = qs.filter(dispatch_date__lte=value)
                        print(f"⚡ Filter: dispatch_date <= {value}")
                    elif field == "incidence_status":
                        qs = qs.filter(incidence__status=value)
                        print(f"⚡ Filter: incidence status = {value}")
                    elif field == "incidence_type":
                        qs = qs.filter(incidence__type=value)
                        print(f"⚡ Filter: incidence type = {value}")
                    elif field == "incidence_date_start":
                        qs = qs.filter(incidence__date__gte=value)
                        print(f"⚡ Filter: incidence date >= {value}")
                    elif field == "incidence_date_end":
                        qs = qs.filter(incidence__date__lte=value)
                        print(f"⚡ Filter: incidence date <= {value}")
                    else:
                        print(f"⚠ Filter ignored, unknown field: {field}")

            # Aplicar ordenamiento
            if page_args.sorting_options:
                order_fields = []
                for s in page_args.sorting_options:
                    field = s.field
                    direction = "" if s.direction == "asc" else "-"
                    if field == "dispatch_date":
                        order_fields.append(f"{direction}{field}")
                if order_fields:
                    qs = qs.order_by(*order_fields)
                    print(f"⚡ Ordering applied: {order_fields}")

            total_count = qs.count()

            # Paginación
            start = page_args.page_index * page_args.page_size
            end = start + page_args.page_size
            qs_page = qs[start:end]
            print(f"📌 Pagination | start={start}, end={end}, page_orders={qs_page.count()}, total_count={total_count}")

            # Mapping
            orders = map_orders(qs_page)
            print(f"✅ Orders mapped to domain entities | total_orders={len(orders)}")

            return QueryResult(
                items=orders,
                page_index=page_args.page_index,
                page_size=page_args.page_size,
                total_count=total_count,
            )

        except Exception as e:
            print(f"❌ Error in get_orders_by_stage: {e}")
            return QueryResult(
                items=[],
                page_index=page_args.page_index,
                page_size=page_args.page_size,
                total_count=0,
                error="There has been an error processing your request",
            )
