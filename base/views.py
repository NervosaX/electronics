from decimal import Decimal

from django.http import Http404

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView
from base.models import Item, ItemCategory, ConversionCategory

# Use form view

class BaseSearchView(object):

    def get_values(self, kwargs):
        vals = {
            'name': kwargs.get("name"),
            'category': kwargs.get("category"),
            'amperageQuery': kwargs.get("selectAmperageQuery"),
            'amperage': kwargs.get("amperage"),
            'voltageQuery': kwargs.get("selectVoltageQuery"),
            'voltage': kwargs.get("voltage"),
            'valuePrefix': kwargs.get("selectPrefix"),
            'value': kwargs.get("value")
        }

        if vals["value"]:
            vals["value"] = int(vals["value"])
        if vals["category"]:
            vals["category"] = int(vals["category"])
        if vals["amperage"]:
            vals["amperage"] = float(vals["amperage"])
        if vals["voltage"]:
            vals["voltage"] = float(vals["voltage"])
        if vals["value"]:
            vals["value"] = float(vals["value"])

        return vals

    def query_data(self, kwargs):

        query = Item.objects.all()
        values = self.get_values(kwargs)

        if values['name']:
            query = query.filter(name__contains=values['name'])
        if values['category']:
            query = query.filter(category=ItemCategory.objects.get(id=values['category']))
        if values['amperage']:
            if values['amperageQuery'] == "=":
                query = query.filter(amperage=values['amperage'])
            elif values['amperageQuery'] == "<":
                query = query.filter(amperage__lt=values['amperage'])
            elif values['amperageQuery'] == ">":
                query = query.filter(amperage__gt=values['amperage'])
        if values['voltage']:
            if values['voltageQuery'] == "=":
                query = query.filter(voltage=values['voltage'])
            elif values['voltageQuery'] == "<":
                query = query.filter(voltage__lt=values['voltage'])
            elif values['voltageQuery'] == ">":
                query = query.filter(voltage__gt=values['voltage'])
        if values['value']:
            decValue = Decimal(values['value'])
            converted = Decimal(values['valuePrefix']) * decValue
            query = query.filter(value_conversion=converted)
        return query


    def get_context_data(self, *args, **kwargs):
        context = super(BaseSearchView, self).get_context_data(
            *args, **kwargs)

        query = self.query_data(self.request.GET).order_by('name')
        paginator = Paginator(query, 10)

        page = self.request.GET.get('page') or 1

        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            page = 1
            items = paginator.page(page)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context.update({
            "categories": ItemCategory.objects.values('id', 'name'),
            "prefixes": ConversionCategory.CHOICES,
            "items": items,
            "form_vals": self.get_values(self.request.GET),
        })
        
        urlString = ""

        for val in context["form_vals"].iterkeys():
            if context["form_vals"][val]:
                urlString += "&%s=%s" % (val, context["form_vals"][val])

        items.previous_link = "?page=%s%s" % (items.previous_page_number(), urlString)
        items.next_link = "?page=%s%s" % (items.next_page_number(), urlString)

        return context


class Index(BaseSearchView, TemplateView):
    template_name = "index.html"


class Detail(BaseSearchView, TemplateView):
    template_name = "detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Detail, self).get_context_data(
            *args, **kwargs)

        id = kwargs.pop('id')
        try:
            item = Item.objects.get(id=id)
        except:
            raise Http404

        context.update({
            "object": item
        })

        return context
