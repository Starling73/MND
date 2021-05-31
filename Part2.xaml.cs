using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace MND_L2a
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class Part2 : ContentPage
    {
        private readonly Picker ratePicker, timePicker, iterationPicker;

        public Part2()
        {
            Title = "Main task";

            var titleLabel = new Label()
            {
                Text = "Perceptron tuning",
                FontSize = Device.GetNamedSize(NamedSize.Title, typeof(Label)),
                VerticalTextAlignment = TextAlignment.Center,
                HorizontalTextAlignment = TextAlignment.Center
            };
            var mainFrame = new Frame
            {
                Content = titleLabel,
                CornerRadius = 8
            };

            var rateLabel = new Label()
            {
                Text = "Model learning rate:",
                FontSize = Device.GetNamedSize(NamedSize.Medium, typeof(Label)),
                VerticalTextAlignment = TextAlignment.Center,
                HorizontalTextAlignment = TextAlignment.Center
            };
            ratePicker = new Picker
            {
                Title = "Choose learning rate",
                FontSize = Device.GetNamedSize(NamedSize.Medium, typeof(Picker)),
                Items = { "0.001", "0.01", "0.05", "0.1", "0.2", "0.3" }
            };
            var firstFlexLayout = new FlexLayout()
            {
                Direction = FlexDirection.Row,
                JustifyContent = FlexJustify.Center,
                Children = { rateLabel, ratePicker }
            };

            var timeLabel = new Label()
            {
                Text = "Time deadline:",
                FontSize = Device.GetNamedSize(NamedSize.Medium, typeof(Label)),
                VerticalTextAlignment = TextAlignment.Center,
                HorizontalTextAlignment = TextAlignment.Center
            };
            timePicker = new Picker
            {
                Title = "Choose time",
                FontSize = Device.GetNamedSize(NamedSize.Medium, typeof(Picker)),
                Items = { "0.5 с", "1 с", "2 с", "5 с" }
            };
            var secondFlexLayout = new FlexLayout()
            {
                Direction = FlexDirection.Row,
                JustifyContent = FlexJustify.Center,
                Children = { timeLabel, timePicker }
            };

            var iterationLabel = new Label()
            {
                Text = "Iterations deadline:",
                FontSize = Device.GetNamedSize(NamedSize.Medium, typeof(Label)),
                VerticalTextAlignment = TextAlignment.Center,
                HorizontalTextAlignment = TextAlignment.Center
            };
            iterationPicker = new Picker
            {
                Title = "Choose iterations count",
                FontSize = Device.GetNamedSize(NamedSize.Medium, typeof(Picker)),
                Items = { "100", "200", "500", "1000" }
            };
            var thirdFlexLayout = new FlexLayout()
            {
                Direction = FlexDirection.Row,
                JustifyContent = FlexJustify.Center,
                Children = { iterationLabel, iterationPicker }
            };

            var solveButton = new Button()
            {
                Text = "Start the process!",
                FontSize = Device.GetNamedSize(NamedSize.Medium, typeof(Button)),
                BorderWidth = 1,
                HorizontalOptions = LayoutOptions.Center,
                VerticalOptions = LayoutOptions.Center,
                TranslationY = 100
            };
            solveButton.Clicked += ShowResult;

            var stackLayout = new StackLayout()
            {
                Margin = 20,
                Spacing = 10,
                Children = { mainFrame, firstFlexLayout, secondFlexLayout, thirdFlexLayout, solveButton }
            };
            Content = stackLayout;
        }

        private async void ShowResult(object sender, EventArgs e)
        {
            if (ratePicker.SelectedIndex == -1 || timePicker.SelectedIndex == -1 || iterationPicker.SelectedIndex == -1)
            {
                await DisplayAlert("Error", "You need to select all perceptron settings.", "Try again");
                return;
            }

            var points = new Point[] { new Point(0, 6), new Point(1, 5), new Point(3, 3), new Point(2, 4) };
            double[] rateData = new double[] { 0.001, 0.01, 0.05, 0.1, 0.2, 0.3 };
            double[] timeData = new double[] { 500, 1000, 2000, 5000 };
            double[] iterationData = new double[] { 100, 200, 500, 1000 };

            const int threshold = 4;
            int solutionsCount = 0;
            var randomGenerator = new Random();
            var overallStartTime = DateTime.Now;

            while ((DateTime.Now - overallStartTime).TotalSeconds <= 5)
            {
                double w1 = 0;
                double w2 = 0;

                int iterationsCount = 0;
                int iterationsPointCount = 0;
                int success = 0;

                int rateChoiceSimulation = randomGenerator.Next(0, 6);
                int timeChoiceSimulation = randomGenerator.Next(0, 4);
                int iterationChoiceSimulation = randomGenerator.Next(0, 4);

                var startTime = DateTime.Now;

                while (iterationsCount < iterationData[iterationChoiceSimulation] && success < 4
                    && (DateTime.Now - startTime).TotalMilliseconds <= timeData[timeChoiceSimulation])

                {
                    int currentPoint = iterationsPointCount % 4;
                    iterationsPointCount++;

                    double y = w1 * points[currentPoint].X + w2 * points[currentPoint].Y;

                    if (((currentPoint < 2) && y >= threshold) || ((currentPoint >= 2) && y < threshold))
                    {
                        success++;
                        continue;
                    }

                    double delta = threshold - y;
                    w1 += delta * points[currentPoint].X * rateData[rateChoiceSimulation];
                    w2 += delta * points[currentPoint].Y * rateData[rateChoiceSimulation];
                    w1 = Math.Ceiling(w1 * Math.Pow(10, 7)) / Math.Pow(10, 7);
                    w2 = Math.Ceiling(w2 * Math.Pow(10, 7)) / Math.Pow(10, 7);
                    success = 0;
                    iterationsCount++;
                }
                solutionsCount++;
            }
            await DisplayAlert("Result", $"Total solutions found in 5 seconds: {solutionsCount}", "Got it!");
        }
    }
}