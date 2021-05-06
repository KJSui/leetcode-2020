using namespace std;
class Counter (
public:
    Counter()
    :m_counter(0){};
    Counter(const Counter &) = delete;
    Counter & operator = (const Counter&) = delete;
    ~Counter(){

    }
    
)