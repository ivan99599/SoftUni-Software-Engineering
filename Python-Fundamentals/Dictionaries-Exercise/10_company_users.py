def company_users():
    companies_data = {}

    while True:
        input_line = input().split(" -> ")
        if input_line[0] == "End":
            break

        company_name, employee_id = input_line
        if company_name not in companies_data:
            companies_data[company_name] = set()

        companies_data[company_name].add(employee_id)

    for company, employees in companies_data.items():
        print(f"{company}")
        for employee in employees:
            print(f"-- {employee}")


# Example usage:
company_users()