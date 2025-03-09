def rate_limiter(ip_address: str, past_requests: dict[str, list[int]], max_requests: int, time_window: int,
                 current_time: int) -> bool:
    return len([ts for ts in past_requests.get(ip_address, []) if ts > current_time - time_window]) < max_requests
