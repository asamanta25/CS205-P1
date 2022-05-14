%% Plot Depth vs. Distance
A_star_misplaced_tile = [0.00, 0.00, 0.00, 0.00, 0.00, 0.03, 0.12, 0.68];
A_star_manhattan_dist = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.02, 0.06];
uniform_cost = [0.00, 0.00, 0.00, 0.02, 0.08, 0.61, 2.86, 11.18];
depths = [0, 2, 4, 8, 12, 16, 20, 24];

hold on;
title("Plot between the Depth  of the solution and the amount of " + ...
    "time taken for each algorithm to find the solution.");
plot(depths, A_star_misplaced_tile);
plot(depths, A_star_manhattan_dist);
plot(depths, uniform_cost);
xlabel("Depth of the solution.");
ylabel("Time taken to finish searching.")
hold off;