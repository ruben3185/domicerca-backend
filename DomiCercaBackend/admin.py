from django.contrib import admin

class AuditAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by',)

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        return obj.save()

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        if 'autocomplete' in request.META['PATH_INFO']:
            queryset = queryset.exclude(active=False)
        return queryset, use_distinct