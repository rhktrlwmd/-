# Этот файл сгенерирован автоматически из qmd-источника.

using DelimitedFiles
using Printf

results_dir = normpath(joinpath(@__DIR__, "..", "results", "data"))
mkpath(results_dir)

function write_csv(path, headers, rows)
    open(path, "w") do io
        println(io, join(headers, ","))
        for row in rows
            println(io, join(string.(row), ","))
        end
    end
end

u0 = 10.0
alpha = 0.35
t_max = 12.0
dt = 0.1
steps = Int(round(t_max / dt))

time = [i * dt for i in 0:steps]
analytic = [u0 * exp(alpha * t) for t in time]
euler = zeros(length(time))
euler[1] = u0
for i in 2:length(time)
    euler[i] = euler[i - 1] + dt * alpha * euler[i - 1]
end

rows = [[@sprintf("%.3f", time[i]), @sprintf("%.6f", analytic[i]), @sprintf("%.6f", euler[i])] for i in eachindex(time)]
write_csv(joinpath(results_dir, "growth_main.csv"), ["time", "analytic", "euler"], rows)

alpha_values = [0.15, 0.25, 0.35, 0.45]
sweep_rows = Vector{Vector{String}}()
for a in alpha_values
    for t in time
        push!(sweep_rows, [@sprintf("%.2f", a), @sprintf("%.3f", t), @sprintf("%.6f", u0 * exp(a * t))])
    end
end
write_csv(joinpath(results_dir, "growth_sweep.csv"), ["alpha", "time", "value"], sweep_rows)
println("lab01 done")
