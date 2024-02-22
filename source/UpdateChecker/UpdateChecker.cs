using Playnite.SDK;
using Playnite.SDK.Events;
using Playnite.SDK.Models;
using Playnite.SDK.Plugins;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.IO;
using System.Diagnostics;
using System.Reflection;

namespace UpdateChecker
{
    

    public class UpdateChecker : GenericPlugin
    {
        private static readonly ILogger logger = LogManager.GetLogger();

        private UpdateCheckerSettingsViewModel settings { get; set; }

        public override Guid Id { get; } = Guid.Parse("74fe180c-7038-4908-bec1-94194b73b2e4");

        public UpdateChecker(IPlayniteAPI api) : base(api)
        {
            settings = new UpdateCheckerSettingsViewModel(this);
            Properties = new GenericPluginProperties
            {
                HasSettings = true
            };
        }


        // Path to python script
        public string py_path = "..\\..\\Roaming\\Playnite\\Extensions\\UpdateChecker_74fe180c-7038-4908-bec1-94194b73b2e4\\manifestreader\\manifestreader.exe";
        public override void OnGameInstalled(OnGameInstalledEventArgs args)
        {
            // Add code to be executed when game is finished installing.
        }

        public override void OnGameStarted(OnGameStartedEventArgs args)
        {
            // Add code to be executed when game is started running.
        }

        public override void OnGameStarting(OnGameStartingEventArgs args)
        {
            // Add code to be executed when game is preparing to be started.
        }

        public override void OnGameStopped(OnGameStoppedEventArgs args)
        {
            // Add code to be executed when game is preparing to be started.
        }

        public override void OnGameUninstalled(OnGameUninstalledEventArgs args)
        {
            // Add code to be executed when game is uninstalled.
        }

        public override void OnApplicationStarted(OnApplicationStartedEventArgs args)
        {
            // Add code to be executed when Playnite is initialized.
            if (settings.Settings.EnableStartup == true)
            {
                if (settings.Settings.EnableFullscreen == false)
                {
                    Process[] pname = Process.GetProcessesByName("Playnite.DesktopApp");
                    if (pname.Length != 0)
                    {
                        System.Diagnostics.Process.Start(py_path);
                    }
                }
                else
                {
                    System.Diagnostics.Process.Start(py_path);
                }
            }



        }

        public override void OnApplicationStopped(OnApplicationStoppedEventArgs args)
        {
            // Add code to be executed when Playnite is shutting down.
        }

        public override void OnLibraryUpdated(OnLibraryUpdatedEventArgs args)
        {
            // Add code to be executed when library is updated.
        }

        public override ISettings GetSettings(bool firstRunSettings)
        {
            return settings;
        }

        public override UserControl GetSettingsView(bool firstRunSettings)
        {
            return new UpdateCheckerSettingsView();
        }

        public override IEnumerable<SidebarItem> GetSidebarItems()
        {
            yield return new SidebarItem
            {
                Title = "Check for game updates",
                // Loads icon from plugin's installation path
                Icon = Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "sidebar_icon.png"),
                ProgressValue = 0,
                Activated = () => System.Diagnostics.Process.Start(py_path)
            };
        }



    }
}