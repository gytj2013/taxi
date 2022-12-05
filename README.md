# taxi

1. gym==0.19.0 버전 맞춰서 다운 받고 taxi.py 파일을 실행시키면 결과를 확인해 볼 수 있다.


2. jupyter notebook (.ipynb) 파일로 실행할 때는   
  1) 'from IPython.display import clear_output' 를 추가하고  
  2) show() 함수 안에  while not terminated : 바로 밑에  
    'clear_output(wait = True)' 를 추가하면 실제로 택시가 움직이는 것처럼 결과를 확인 할 수 있다. 
