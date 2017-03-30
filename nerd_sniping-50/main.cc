#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;

int main()
{
    // Obviously, the number of test cases input is going to be important. Store that off first.
    uint32_t t = 0u;
    cin >> t;

    // I'm going to read in every value ahead of time, so that I can keep track of the maximum value.
    //  I'm using the Sieve of Eratosthenes to find all the prime numbers needed, but in order to do so,
    //  a buffer of size (n) needs to be pre-allocated. I need to know what the largest number I might
    //  come across will be.
    vector<uint32_t> A, B, K;
    A.reserve(t);
    B.reserve(t);
    K.reserve(t);

    uint32_t max = 0u;

    vector<uint32_t> S;

    for (uint32_t idx = 0u; idx < t; idx++)
    {
        uint32_t a, b, k;
        cin >> a >> b >> k;
        A.push_back(a);
        B.push_back(b);
        K.push_back(k);

        if (b > max) max = b;
    }

    // Resize the vector (and zero out all the new elements)
    S.resize(max + 1, 0u);

    // Execute the Sieve of Eratosthenes
    //
    // Memory Complexity: O(N)
    // Runtime Complexity: O(N^2)-ish (better because second iterator is not over N, but by N/2, then N/3, then N/5...)
    //
    // A naive solution could feasibly be O(N^3) in runtime or worse
    for (uint32_t idx = 2; idx <= max; idx++)
    {
        // If we hit a number X that is zero in the array, it is a prime number. Keep it zero, and
        //  increment every element in the array equal to N * X for all N >= 2. This increases the
        //  primacity score of said element by one for this prime
        // This also has the pleasant side effect that the value of each number in the array is also
        //  its primacity. There will be no non-prime number with a primacity of 0.
        if (S[idx] == 0u)
        {
            for (uint32_t stride = idx; stride <= max; stride += idx)
            {
                S[stride]++;
            }
        }
    }

    // Now iterate between A and B for each case (inclusive), and output the number of elements in S that have the value
    //  requested in K.
    for (uint32_t testNumber = 0; testNumber < t; testNumber++)
    {
        uint32_t count = 0u;
        uint32_t k = K[testNumber]; // Cache optimization probably not needed - compilers are pretty good at this (they can get the A[], B[] below)

        for (uint32_t idx = A[testNumber]; idx <= B[testNumber]; idx++)
        {
            if (S[idx] == k)
            {
                count++;
            }
        }

        cout << count << endl;
    }

    return 0;
}