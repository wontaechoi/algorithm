T= int(input())
for test_case in range(1, T+1):
    N, M, K, A, B = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    customers = list(map(int, input().split()))

    for i in range(len(customers)):
        customers[i] = (i, customers[i])


    using_a = [0 for i in range(N)]
    using_b = [0 for i in range(M)]
    at_a = []
    waiting_b = []
    at_b = []
    t = 0
    completed = 0
    visited_A = []
    visited_B = []
    waiting_a = []
    while True:
        new_at_b = []
        for cust in at_b:
            cust_num, b_num, cust_time = cust
            if cust_time - 1 != 0:
                new_at_b.append((cust_num, b_num, cust_time - 1))
            else:
                using_b[b_num] = 0
                completed += 1
        at_b = new_at_b
        new_at_a = []
        for cust in at_a:
            cust_num, a_num, cust_time = cust
            if cust_time - 1 != 0:
                new_at_a.append((cust_num, a_num, cust_time - 1))
            else:
                using_a[a_num] = 0
                waiting_b.append((cust_num, a_num, t))
        at_a = new_at_a
        found = False

        waiting_b.sort(key = lambda x: [x[2], x[1], x[0]])
        max_ind = 0
        for index, (cust, a_num, time) in enumerate(waiting_b):
            found = False
            for i in range(len(using_b)):
                if using_b[i] == 0:
                    found = True
                    using_b[i] = 1
                    at_b.append((cust, i, b[i]))
                    max_ind = index + 1
                    if i + 1 == B:
                        visited_B.append(cust + 1)
                    break
            if not found:
                break
        waiting_b = waiting_b[max_ind:]
        max_ind = 0

        new_customers = []
        for index, (customer, time) in enumerate(customers):
            found = False
            if time <= t:
                waiting_a.append(customer)
            else:
                new_customers.append((customer, time))
        customers = new_customers
        waiting_a.sort()

        for index, customer in enumerate(waiting_a):
            found = False
            for i in range(len(using_a)):
                if using_a[i] == 0:
                    found = True
                    using_a[i] = 1
                    at_a.append((customer, i, a[i]))
                    max_ind = index + 1
                    if i + 1 == A:
                        visited_A.append(customer + 1)
                    break
            if not found:
                break


        waiting_a = waiting_a[max_ind:]
        if not customers and not waiting_a and not at_a and not waiting_b:
            break

        t += 1
    answer = sum(list(set(visited_A).intersection(visited_B)))
    answer = -1 if answer == 0 else answer
    print("#{} {}".format(test_case, answer))