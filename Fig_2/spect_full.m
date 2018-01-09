
x=UE;

N = length(x);
Fs=1/dt;

xdft = fft(x);
xdft = xdft(1:N/2+1);
psdx = (1/(Fs*N)) * abs(xdft).^2;
psdx(2:end-1) = 2*psdx(2:end-1);
freq = 0:Fs/length(x):Fs/2;

power=10*log10(psdx);

max_power=abs(max(power(1:end)));
%plot(freq,power/max_power); 
%plot(freq,psdx); 
% /max(power(100:end)) % normalise the spectrum by its max
grid on
set(gca,'FontSize',20);             % set the axis with big font
xlabel('Frequency (Hz)')
ylabel('Power/Frequency')

max(psdx(100:end)); % postition of the maximal peak


f_max=find(psdx==max(psdx(100:end))); % peak location index
                                      % 100 to get rid of the nonsense peak