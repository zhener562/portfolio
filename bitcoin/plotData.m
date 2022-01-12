clear
data = load('bitcoinPrice.tex');
y = data(:, 2);
m = length(y); % number of training examples
X = [ones(m, 1), data(:,1),data(:,1).^2]; % Add a column of ones to x
%theta = zeros(3, 1); % initialize fitting parameters
theta=inv(X'*X)*(X'*y)
plot(data(:, 1),data(:, 2))
hold on
htheta=X*theta;
plot(data(:, 1),htheta)
corr(data(:,1),htheta)