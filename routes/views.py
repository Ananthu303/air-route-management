from django.shortcuts import render
from django.views import View
from .forms import AirportRouteForm, SearchForm, ShortestPathForm
from .models import AirportRoute
from .utils import RouteUtils


class AddAirportRouteView(View):
    template_name = "routes/add_route.html"

    def get(self, request):
        form = AirportRouteForm()
        routes = AirportRoute.objects.all().order_by('position')
        return render(request, self.template_name, {"form": form, "routes": routes, "message": ""})

    def post(self, request):
        form = AirportRouteForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Airport added successfully!"
            form = AirportRouteForm()
        else:
            message = "Please correct the errors below."
        routes = AirportRoute.objects.all().order_by('position')
        return render(request, self.template_name, {"form": form, "routes": routes, "message": message})


class FindNthNodeView(View):
    template_name = "routes/find_nth_node.html"

    def get(self, request):
        form = SearchForm()
        return render(request, self.template_name, {"form": form, "result": None})

    def post(self, request):
        form = SearchForm(request.POST)
        result = None
        message = ""
        if form.is_valid():
            start_code = form.cleaned_data["start_code"]
            n = form.cleaned_data["n"]
            direction = form.cleaned_data["direction"]
            try:
                start_node = AirportRoute.objects.get(airport_code=start_code)
                result = RouteUtils.get_nth_node(start_node, n, direction)
                if result is None:
                    message = f"Cannot find the {n}th node in the '{direction}' direction from {start_code}."
            except AirportRoute.DoesNotExist:
                message = f"Airport code '{start_code}' does not exist."

        return render(
            request,
            self.template_name,
            {"form": form, "result": result, "message": message},
        )


class LongestNodeView(View):
    template_name = "routes/longest_node.html"

    def get(self, request):
        node = RouteUtils.get_longest_node()
        return render(request, self.template_name, {"node": node})


class ShortestDurationView(View):
    template_name = "routes/shortest_duration.html"

    def get(self, request):
        form = ShortestPathForm()
        return render(
            request, self.template_name, {"form": form, "result": None, "message": ""}
        )

    def post(self, request):
        form = ShortestPathForm(request.POST)
        result = None
        message = ""
        if form.is_valid():
            start_code = form.cleaned_data["start_code"]
            end_code = form.cleaned_data["end_code"]
            result = RouteUtils.get_shortest_duration(start_code, end_code)
            if result is None:
                message = f"No route from {start_code} to {end_code}"
        return render(
            request,
            self.template_name,
            {"form": form, "result": result, "message": message},
        )
