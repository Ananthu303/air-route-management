from .models import AirportRoute


class RouteUtils:
    """
    Utility class for performing operations on AirportRoute linked list.
    """

    @staticmethod
    def get_nth_node(start_node, n, direction):
        """
        Returns the nth node in the given direction (left/right) from start_node.
        """
        current = start_node
        count = 0
        while count < n:
            if direction == "right":
                if current.next_node:
                    current = current.next_node
                else:
                    return None
            elif direction == "left":
                prev_nodes = current.previous_node.all()
                if prev_nodes.exists():
                    current = prev_nodes[0]
                else:
                    return None
            count += 1
        return current

    @staticmethod
    def get_longest_node():
        """
        Returns the AirportRoute node with the longest duration to the next airport.
        """
        return AirportRoute.objects.order_by("-duration").first()

    @staticmethod
    def get_shortest_duration(start_code, end_code):
        """
        Returns total duration from start_code to end_code in either direction.
        Returns None if end is not reachable.
        """
        try:
            start = AirportRoute.objects.get(airport_code=start_code)
            end = AirportRoute.objects.get(airport_code=end_code)
        except AirportRoute.DoesNotExist:
            return None

        current = start
        total_duration = 0
        while current != end:
            if current.next_node:
                total_duration += current.duration
                current = current.next_node
            else:
                break
        else:
            return total_duration

        current = start
        total_duration = 0
        while current != end:
            prev_nodes = current.previous_node.all()
            if prev_nodes.exists():
                prev = prev_nodes[0]
                total_duration += prev.duration
                current = prev
            else:
                return None
        return total_duration
