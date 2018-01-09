% Bifurcation processing


%% gAHP
% load gAHP.dat
plot(gAHP(1:20),UE_1(1:20),gAHP(43:89),UE_1(43:89),gAHP(90:139),UE_1(90:139),gAHP(242:320),UE_1(242:320),gAHP(242:320),UE_2(242:320))
xlabel('g_{AHP} (uS/cm^2)')
ylabel('U_E (mV)')
set(gca,'Fontsize',30)
%%

%% gEE
% load gEE.dat
plot(gEE(1:20),UE_1(1:20),gEE(21:56),UE_1(21:56),gEE(57:126),UE_1(57:126),gEE(128:326),UE_1(128:326),gEE(128:326),UE_2(128:326))
xlabel('g_{EE} (uS/cm^2)')
ylabel('U_E (mV)')
set(gca,'Fontsize',30)
%%

%% gEI
% load gEI.dat
plot(gEI(1:50),UE_1(1:50),gEI(71:140),UE_1(71:140),gEI(141:289),UE_1(141:289),gEI(290:485),UE_1(290:485),gEI(290:488),UE_2(290:488),gEI(490:689),UE_2(490:689),gEI(490:689),UE_1(490:689))
xlabel('g_{EI} (uS/cm^2)')
ylabel('U_E (mV)')
set(gca,'Fontsize',30)
%%

%% gIE
% load gIE.dat
plot(gIE(1:85),UE_1(1:85),gIE(86:117),UE_1(86:117),gIE(118:290),UE_1(118:290),gIE(118:290),UE_2(118:290))
xlabel('g_{IE} (uS/cm^2)')
ylabel('U_E (mV)')
set(gca,'Fontsize',30)
%%

%% gII
% load gII.dat
plot(gII(1:21),UE_1(1:21),gII(22:65),UE_1(22:65),gII(66:124),UE_1(66:124),gII(66:124),UE_2(66:124),gII(126:324),UE_2(126:324))
xlabel('g_{II} (uS/cm^2)')
ylabel('U_E (mV)')
set(gca,'Fontsize',30)
%%

%% VGABA
% load VGABA.dat
plot(VGABA(1:41),UE_1(1:41),VGABA(42:67),UE_1(42:67),VGABA(68:200),UE_1(68:200),VGABA(201:280),UE_1(201:280),VGABA(201:280),UE_2(201:280))
xlabel('V_{GABA} (mV)')
ylabel('U_E (mV)')
set(gca,'Fontsize',30)
%%