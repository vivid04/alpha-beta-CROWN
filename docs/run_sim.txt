set method=%1
set cfgName=mnist_6_100_bab_%method%


cd "D:\wordspace\python\alpha-beta-CROWN\complete_verifier"
d:

for %%e in (0.01,0.02,0.04) do 
cmd /C "C:\ProgramData\Anaconda3\envs\nnv\python.exe  robustness_verifier.py --config exp_configs/%cfgName% .yaml --branching_method %method% --epsilon %%e --timeout 1 --end 3 >>rec%cfgName%_eps_%%e.txt" 
