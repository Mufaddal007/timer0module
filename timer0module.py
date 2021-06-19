osc_freq,pslr_val,delay=map(int,input('Enter:- OscillatorFrequency(Hertz)  PrescalerValue     Delay(ms): ').split())
reg_val=256-((osc_freq*(delay*pow(10,-3))/(4*pslr_val)))
cal_val=(((256-reg_val)*(4*pslr_val))/osc_freq)*1000
print(cal_val)
