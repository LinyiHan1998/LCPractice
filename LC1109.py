def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
    flights = [0] * n
    diff = [0] * n
    for b in bookings:
        diff[b[0]-1] += b[2]
        if b[1]<n:
            diff[b[1]] -= b[2]
    flights[0] = diff[0]
    for i in range(1,n):
        flights[i] = diff[i]+flights[i-1]
    return flights