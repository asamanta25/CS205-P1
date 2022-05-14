%% Plot Depth vs. Time
A_star_misplaced_tile = [0.00, 0.00, 0.00, 0.00, 0.00, 0.03, 0.12, 0.68];
A_star_manhattan_dist = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.02, 0.06];
uniform_cost = [0.00, 0.00, 0.00, 0.02, 0.08, 0.61, 2.86, 11.18];
depths = [0, 2, 4, 8, 12, 16, 20, 24];

hold on;
title("Depth vs. Time.");
plot(depths, A_star_misplaced_tile, 'DisplayName', "A* Misplaced Tile");
plot(depths, A_star_manhattan_dist, 'DisplayName', "A * Manhattan Distance");
plot(depths, uniform_cost, 'DisplayName', "Uniform Cost");
xlabel("Depth of the solution.");
ylabel("Time taken to finish searching.")
hold off;