
%% extract the data
h = findobj(gca,'Type','line');

time = get(h,'Xdata');
signal = get(h,'Ydata');

%%