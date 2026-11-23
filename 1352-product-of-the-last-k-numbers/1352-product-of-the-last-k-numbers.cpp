class ProductOfNumbers {
public:
     vector<int> arr;
    ProductOfNumbers() {
       
    }
    
    void add(int num) {
        arr.push_back(num);

        
    }
    
    int getProduct(int k) {
        int n = arr.size();
        int product = 1;
        for(int i=n- k;i<n;i++){
            product = product * arr[i];
        }
        return product;
        
        
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */