using Playnite.SDK;
using Playnite.SDK.Data;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;
using System.Windows;

namespace UpdateChecker
{
    public class UpdateCheckerSettings : ObservableObject
    {
        private bool enablefullscreen = false;
        private int path_slider = 1;
        private string steampath = String.Empty;
        private string steampath2 = String.Empty;
        private string steampath3 = String.Empty;
        private string steampath4 = String.Empty;
        private string steampath5 = String.Empty;
        private bool enablestartup = false;
        private bool enablesteam = true;
        private bool enableepic = true;

        public bool EnableFullscreen { get => enablefullscreen; set => SetValue(ref enablefullscreen, value); }
        public int PathSlider { get => path_slider; set => SetValue(ref path_slider, value); }
        public string SteamPath { get => steampath; set => steampath = value; }
        public string SteamPath2 { get => steampath2; set => steampath2 = value; }
        public string SteamPath3 { get => steampath3; set => steampath3 = value; }
        public string SteamPath4 { get => steampath4; set => steampath4 = value; }
        public string SteamPath5 { get => steampath5; set => steampath5 = value; }
        public bool EnableStartup { get => enablestartup; set => SetValue(ref enablestartup, value); }
        public bool EnableSteam { get => enablesteam; set => SetValue(ref enablesteam, value); }
        public bool EnableEpic { get => enableepic; set => SetValue(ref enableepic, value); }
        // Playnite serializes settings object to a JSON object and saves it as text file.
        // If you want to exclude some property from being saved then use `JsonDontSerialize` ignore attribute.

    }



    public class UpdateCheckerSettingsViewModel : ObservableObject, ISettings
    {
        private readonly UpdateChecker plugin;
        private UpdateCheckerSettings editingClone { get; set; }

        private UpdateCheckerSettings settings;
        public UpdateCheckerSettings Settings
        {
            get => settings;
            set
            {
                settings = value;
                OnPropertyChanged();
            }
        }

        public UpdateCheckerSettingsViewModel(UpdateChecker plugin)
        {
            // Injecting your plugin instance is required for Save/Load method because Playnite saves data to a location based on what plugin requested the operation.
            this.plugin = plugin;

            // Load saved settings.
            var savedSettings = plugin.LoadPluginSettings<UpdateCheckerSettings>();


            // LoadPluginSettings returns null if no saved data is available.
            if (savedSettings != null)
            {
                Settings = savedSettings;
            }
            else
            {
                Settings = new UpdateCheckerSettings();
            }
        }

        public void BeginEdit()
        {
            // Code executed when settings view is opened and user starts editing values.
            editingClone = Serialization.GetClone(Settings);
        }

        public void CancelEdit()
        {
            // Code executed when user decides to cancel any changes made since BeginEdit was called.
            // This method should revert any changes made to enablefullscreen and Option2.
            Settings = editingClone;
        }

        public void EndEdit()
        {
            // Code executed when user decides to confirm changes made since BeginEdit was called.
            // This method should save settings made to enablefullscreen and Option2.
            plugin.SavePluginSettings(Settings);

        }

        public bool VerifySettings(out List<string> errors)
        {
            // Code execute when user decides to confirm changes made since BeginEdit was called.
            // Executed before EndEdit is called and EndEdit is not called if false is returned.
            // List of errors is presented to user if verification fails.
            errors = new List<string>();
            return true;
        }
    }
}