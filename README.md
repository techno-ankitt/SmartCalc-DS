# Ankit's Smart Calculator

### Project Concept: Dukandari aur Hunar (Merchant & Skill)
Maine is code ko ek "Dukandari" ke model par banaya hai taaki logic hamesha yaad rahe:

1. **Hunar (The Function - `ankit_calculator`):**
   Ye is project ki "Skill" hai. Iska kaam hai math solve karna. Jaise halwai ko jalebi banana aata hai, waise hi is function ko calculations aati hain.

2. **Dukaan (The Main Execution - `main`):**
   Ye wo jagah hai jahan user (customer) aata hai. Ye input leta hai aur result dikhata hai.

3. **Dukaan ka Shutter (The Entry Point):**
   `if __name__ == "__main__":` ye check karta hai ki dukaan khulni chahiye ya nahi.
   (entry point ka sbse bda faayda ye hai ki hum code ke structure ke kisi dusre code me daal skte hai lekin eski value hai vo dusre code me nhi jayegi, mtlb hum halwai ki skills jalebi bnana to har kahi kar le ja skte hai lekin hum uske data mtlb uski dukan ko har kahi nhi le ja skte hai)
   
### 1. Requirements
Is code ko chalane ke liye `numexpr` library zaroori hai:
```bash
pip install numexpr
python SmartCalc-DS.py
   
(maine es code se 2 sbse important cheez sikhi one is numexpr aur second is my fevorite `if __name__ == "__main__")
*Created by Ankit | B.Tech Data Science Student*
   
