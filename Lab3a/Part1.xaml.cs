using System;
using System.Collections.Generic;

using Xamarin.Forms;

namespace MND_L3a
{
    public partial class Part1 : ContentPage
    {
        private readonly Entry aEntry;
        private readonly Entry bEntry;
        private readonly Entry cEntry;
        private readonly Entry dEntry;
        private readonly Entry yEntry;

        public Part1()
        {
            Title = "Main task";

            StackLayout stackLayout = new StackLayout()
            {
                Margin = 20,
                Spacing = 30
            };

            var titleLabel = new Label()
            {
                Text = "Genetic algorithm",
                FontSize = Device.GetNamedSize(NamedSize.Title, typeof(Label)),
                VerticalTextAlignment = TextAlignment.Center,
                HorizontalTextAlignment = TextAlignment.Center
            };

            aEntry = new Entry()
            {
                Placeholder = "Enter A coeff",
                Keyboard = Keyboard.Numeric
            };

            bEntry = new Entry()
            {
                Placeholder = "Enter B coeff",
                Keyboard = Keyboard.Numeric
            };

            cEntry = new Entry()
            {
                Placeholder = "Enter C coeff",
                Keyboard = Keyboard.Numeric
            };

            dEntry = new Entry()
            {
                Placeholder = "Enter D coeff",
                Keyboard = Keyboard.Numeric
            };

            yEntry = new Entry()
            {
                Placeholder = "Enter Y",
                Keyboard = Keyboard.Numeric
            };

            var solveButton = new Button()
            {
                Text = "Start the process!",
                FontSize = Device.GetNamedSize(NamedSize.Medium, typeof(Button)),
                HorizontalOptions = LayoutOptions.Center,
                VerticalOptions = LayoutOptions.Center,
            };
            solveButton.Clicked += Genetic;



            stackLayout.Children.Add(titleLabel);
            stackLayout.Children.Add(aEntry);
            stackLayout.Children.Add(bEntry);
            stackLayout.Children.Add(cEntry);
            stackLayout.Children.Add(dEntry);
            stackLayout.Children.Add(yEntry);
            stackLayout.Children.Add(solveButton);

            Content = stackLayout;
        }
        public async void Genetic(object sender, EventArgs e)
        {
            Double.TryParse(aEntry.Text, out double a);
            Double.TryParse(bEntry.Text, out double b);
            Double.TryParse(cEntry.Text, out double c);
            Double.TryParse(dEntry.Text, out double d);
            Double.TryParse(yEntry.Text, out double y);
            Random random = new Random();
            bool Succesful = false;
            double[][] population = new double[4][];
            population[0] = new double[4]; 
            population[1] = new double[4];
            population[2] = new double[4];
            population[3] = new double[4];
            var startTime = DateTime.Now;
            for (int i = 0; i < population.Length; i++)
            {
                for (int j = 0; j < population[i].Length; j++)
                {
                    population[i][j] = (int)(1 + random.NextDouble() * (y / 2));
                }
            }
            while (!Succesful)
            {
                double[] delta = new double[4];
                double roulette_parameter = 0;
                double[] chance_of_parenthood = new double[4];
                for (int i = 0; i < 4; i++)
                {
                    delta[i] = Math.Abs(y - (a * population[i][0] + b * population[i][1] + c * population[i][2] + d * population[i][3]));
                    roulette_parameter += 1 / delta[i];
                    if (delta[i] == 0)
                    {
                        Succesful = true;
                        await DisplayAlert("Result", $"Знайдені корені рівняння:\nX1 = {population[i][0]}\nX2 = {population[i][1]}\n" +
                            $"X3 = {population[i][2]}\nX4 = {population[i][3]}\n" +
                            $"Execution time = {(DateTime.Now - startTime).TotalMilliseconds} ms\n", "Got it!");
                        break;
                    }
                }
                
                chance_of_parenthood[0] = 1 / delta[0] / roulette_parameter;
                for (int i = 1; i < 4; i++)
                {
                    chance_of_parenthood[i] = chance_of_parenthood[i - 1] + 1 / delta[i] / roulette_parameter;
                }
                double chance1 = random.NextDouble();
                double chance2 = random.NextDouble();
                double chance3 = random.NextDouble();
                double chance4 = random.NextDouble();
                double[] father1 = new double[4];
                double[] father2 = new double[4];
                double[] father3 = new double[4];
                double[] father4 = new double[4];
                //знаходження 1 та 2 батьків
                for (int i = 0; i < 4; i++)
                {
                    if (chance1 < chance_of_parenthood[i])
                    {
                        father1 = population[i];
                        for (int j = 0; j < 4; j++)
                        {
                            if (chance2 < chance_of_parenthood[j])
                            {

                                father2 = population[j];
                                break;
                            }
                        }
                        break;
                    }
                }
                //знаходження 3 та 4 батьків
                for (int i = 0; i < 4; i++)
                {
                    if (chance3 < chance_of_parenthood[i])
                    {
                        father3 = population[i];
                        for (int j = 0; j < 4; j++)
                        {
                            if (chance4 < chance_of_parenthood[j])
                            {
                                father4 = population[j];
                                break;
                            }
                        }
                        break;
                    }
                }
                //кросовер 1 та 2 батьків
                int index1 = random.Next(3);
                for (int i = 0; i <= index1; i++)
                {
                    double k = father1[i];
                    father1[i] = father2[i];
                    father2[i] = k;
                }
                //кросовер 3 і 4 батьків
                int index2 = random.Next(3);
                for (int i = 0; i <= index2; i++)
                {
                    double k = father3[i];
                    father3[i] = father4[i];
                    father4[i] = k;
                }
                //нова популяція
                population = new double[][] { father1, father2, father3, father4 };

                double chance_of_mutation = random.NextDouble();
                //шанс мутації 20%
                if (chance_of_mutation < 0.2)
                {
                    int mutation = random.Next(2);
                    if (mutation == 0)
                        population[random.Next(4)][random.Next(4)] += 1;
                    else population[random.Next(4)][random.Next(4)] -= 1;
                }

            }
        }
    }
}
