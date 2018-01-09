%% Plot spectrum

figure

spect(t,UE,1000);

%%

%% Plot time series

figure

plot(t/1000,UE);
set(gca,'Fontsize',30);
title('Oscillations');
xlabel('Time(s)');
ylabel('U_E(mV)');

%%