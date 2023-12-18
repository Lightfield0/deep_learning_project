from django.contrib import admin
from .models import TeamMember, Contact

admin.site.register(TeamMember)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Listeleme sayfasında gösterilecek alanlar
    search_fields = ('name', 'email')  # Arama yapılacak alanlar
    readonly_fields = ('created_at',)  # Sadece okunabilir alanlar
