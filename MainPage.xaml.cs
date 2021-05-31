using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace MND_L2a
{
    public partial class MainPage : TabbedPage
    {
        public MainPage()
        {
            Children.Add(new Part2());
        }
    }
}
