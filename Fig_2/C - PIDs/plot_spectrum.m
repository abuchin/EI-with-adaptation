
%% clean up

close all;
%clear;


%%



%% Plot the oscillatory spectrum using multitaper method

% multitaper method

% temporal discretization
dt=(time(2)-time(1))*1000;

fs = 1/dt*1000;


% normalize the data
signal=signal-mean(signal);
%% plot the spectrum

% create a new figure
figure;

b=(0:0.001:0.03);
[a,b] =pmtm(signal,10,length(signal),fs,'unity');
plot(b,a/max(a));
% limit the fruency range, in Hz
xlim([0, 15]);
set(gca,'Fontsize',10);
title('Power spectrum')
box off;

%%



