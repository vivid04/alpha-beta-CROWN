g`"et cfgName=mnist_6_100_bab
set timeout=40
set endID=100

set method=rlm
for %e in (0.01,0.02,0.03) do  cmd /C "C:\ProgramData\Anaconda3\envs\nnv\python.exe  robustness_verifier.py --config exp_configs/%cfgName%_%method%.yaml --branching_method %method% --epsilon %e --timeout %timeout%  --end %endID% >>rec%cfgName%_%method%_eps_%e.txt" 

set method=fsb
for %e in (0.01,0.02,0.03) do  cmd /C "C:\ProgramData\Anaconda3\envs\nnv\python.exe  robustness_verifier.py --config exp_configs/%cfgName%_%method%.yaml --branching_method %method% --epsilon %e --timeout %timeout% --end %endID% >>rec%cfgName%_%method%_eps_%e.txt" 

set method=babsr
for %e in (0.01,0.02,0.03) do  cmd /C "C:\ProgramData\Anaconda3\envs\nnv\python.exe  robustness_verifier.py --config exp_configs/%cfgName%_%method%.yaml --branching_method %method% --epsilon %e --timeout %timeout% --end %endID% >>rec%cfgName%_%method%_eps_%e.txt" 

set method=random
for %e in (0.01,0.02,0.03) do  cmd /C "C:\ProgramData\Anaconda3\envs\nnv\python.exe  robustness_verifier.py --config exp_configs/%cfgName%_%method%.yaml --branching_method %method% --epsilon %e --timeout %timeout% --end %endID% >>rec%cfgName%_%method%_eps_%e.txt" 

https://github.com/vivid04/alpha-beta-CROWN












 cmd /C "C:\ProgramData\Anaconda3\envs\nnv\python.exe  robustness_verifier.py --help"


for %strategy in ("rlm","fsb","random","sr") do @echo %strategy
