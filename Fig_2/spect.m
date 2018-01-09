function [a,b] = spect(t,S,N)
%UNTITLED3 Summary of this function goes here
%   Computes the FFT and plots the spectrum

Y = fft(S,length(S));
Pyy = Y.*conj(Y)/length(S);
Pyy = Pyy/sum(Pyy);                % normalization of the spectrum

f = 1000/(t(2)-t(1))/length(S)*(0:N); % vector of frequencies

plot(f,Pyy(1:length(f)));
set(gca,'FontSize',20);           % make all the font sizes big

title('E');
xlabel('Frequency, Hz');
ylabel('Power');

a=f;
b=Pyy(1:length(f));

end
