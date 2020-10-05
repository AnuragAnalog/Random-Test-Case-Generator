#include <bits/stdc++.h> 
#define pb push_back
#define mp make_pair 
#define fr first
#define sc second
#define MOD 1000000007
#define len(x) x.size()
#define min3(a, b, c) min(a, min(b, c))
#define max3(a, b, c) max(a, max(b, c))
#define all(v) v.begin(), v.end()
#define alla(a,n) a, a + n
  
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<pll> vpll;
typedef vector<vll> vvll;
typedef vector<string> vs;
int randomize()
{
    return (rand() % 1000);
}
int32_t main() {

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin) ;
    freopen("output.txt", "w", stdout) ;
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL) ; cout.tie(NULL) ;

    int t ;
    cin >> t ;

    while( t-- ) {
        // for different values each time we run the code
        srand(time(NULL));
        int num;
        cin>>num;

        vector<int> vect(num); // declaring the vector

        // Fill all elements using randomize()
        generate(vect.begin(), vect.end(), randomize);

        // displaying the content of vector
        for (int i=0; i<vect.size(); i++)
                cout << vect[i] << " " ;

    }

    return 0 ;

}