   M S B A M L   `   `   `  ����  UpdateChecker-    'UpdateChecker.UpdateCheckerSettingsView   5      R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35G CPlaynite.SDK, Version=6.2.0.0, Culture=neutral, PublicKeyToken=null\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35F 9http://schemas.microsoft.com/winfx/2006/xaml/presentation     5      R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5      Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5      @d2http://schemas.microsoft.com/expression/blend/2008     5        � 	Resources  5         
steampath2 �� 
TargetType �� Property �� Value �� Triggers �� Binding �� ElementName �� Path �� Value  
steampath3  
steampath4  
steampath5��%P  &	        &	 A    &	     &	 U    �� 5	   
   " ]�6$   .�5
      ��  � y�$ Hidden=�6+    5      �� 5       6   �� $ path_slider��$ Value� 26V   .a�5      ��  � y�$ Visible=�63   5      �� 5       6   �� $ path_slider��$ Value� 36V   .a�5      ��  � y�$ Visible=�63   5      �� 5       6   �� $ path_slider��$ Value� 46V   .a�5      ��  � y�$ Visible=�63   5      �� 5       6   �� $ path_slider��$ Value� 56V   .a�5      ��  � y�$ Visible=�63   5      5      �� 5   
   " ]�6$   .�5      ��  � y�$ Hidden=�6+    5      �� 5       6   �� $ path_slider��$ Value� 36V   .a�5       ��  � y�$ Visible=�63   5!      �� 5"       6   �� $ path_slider��$ Value� 46V   .a�5#      ��  � y�$ Visible=�63   5$      �� 5%       6   �� $ path_slider��$ Value� 56V   .a�5&      ��  � y�$ Visible=�63   5'      5)      �� 5*   
   " ]�6$   .�5+      ��  � y�$ Hidden=�6+    5,      �� 5.       6   �� $ path_slider��$ Value� 46V   .a�5/      ��  � y�$ Visible=�63   50      �� 51       6   �� $ path_slider��$ Value� 56V   .a�52      ��  � y�$ Visible=�63   53      55      �� 56   
   " ]�6$   .�57      ��  � y�$ Hidden=�6+    58      �� 5:       6   �� $ path_slider��$ Value� 56V   .a�5;      ��  � y�$ Visible=�63   5<      5>      5A      .��5C      �� .+�5D   
   �� $��Update Checker��6   $��49��6*   $	��684��66   $��30(�6B   $��SemiBold"�6P   �� 5E   
   $��	Settings:��6   $��23��6%   $	��603��61   �� 5F   
   -   5        $��startupenable��5F      	 d� 	IsChecked	 6(   �� *Settings.EnableStartup+.��5G      �� $��Show on startup��6   5H      �� 5J   
   -   5        $��30,0,0,0q�5J      {�6%   �� $ startupenable��$ 	IsChecked�	 6e   �� *Settings.EnableFullscreen+.��5K      �� $��Show in Fullscreen Mode��6   5L      �� 5M   
   -   5        $��enablesteam��5M      $��0,0,0,0q�6&   	 67   �� *Settings.EnableSteam+.��5N      �� $��Enable Steam support��6   5O      ]� 5Q   
   
 � ToolTip$0
 *e.g C:/Program Files (x86)/Steam/steamapps��6   $��	30,0,0,10q�6�   $
��Left=�6�   $	��350��6�   $��21��6�   {�6I   �� $ enablesteam��$ 	IsChecked�.+�5R      �� $��Number of paths: ��6   $��0,0,10,0q�61   $
��Left=�6C   $��15��6^   $	��Top=�6j   �� 5S      -   5        $��path_slider��5S       � Maximum$ 5Q�6N    � Minimum$ 1Q�6Z   $	��200��6f    �� IsSnapToTickEnabled .  �� TickFrequency$ 1Q�6�    � Value 6(   �� *Settings.PathSlider+6�   �� 5T      $��10,0,0,0q�6M   $
��Left=�6_   $��15��6z   $	��Top=�6�   ��6   �� $ path_slider��$ Value�6�   5U      ]� 5X   
   $0
 *e.g C:/Program Files (x86)/Steam/steamapps��6   $��	30,0,0,10q�6�   $
��Left=�6�   $	��350��6�   $��21��6�   {�6I   �� $ enablesteam��$ 	IsChecked�.+�5Y      �� $��Path:��6   $
��Left=�6%   $��15��6@   $	��Top=�6L   �� 5Z      $��10,0,0,0q�6   $��20��6L   $	��Top=�6X   $	��300��6p   ��6(   �� *Settings.SteamPath+6p   5[      ]� 5]   
   #��[  6   $0
 *e.g C:/Program Files (x86)/Steam/steamapps��68   $��	30,0,0,10q�6�   $
��Left=�6�   $	��350��6�   $��21��6�   {�6m   �� $ enablesteam��$ 	IsChecked�.+�5^      �� $��Path 2:��6   $
��Left=�6'   $��15��6B   $	��Top=�6N   �� 5_      $��10,0,0,0q�6   $��20��6M   $	��Top=�6Y   $	��300��6q   ��6(   �� *Settings.SteamPath2+6q   5`      ]� 5b   
   #��[ 6   $0
 *e.g C:/Program Files (x86)/Steam/steamapps��68   $��	30,0,0,10q�6�   $
��Left=�6�   $	��350��6�   $��21��6�   {�6m   �� $ enablesteam��$ 	IsChecked�.+�5c      �� $��Path 3:��6   $
��Left=�6'   $��15��6B   $	��Top=�6N   �� 5d      $��10,0,0,0q�6   $��20��6M   $	��Top=�6Y   $	��300��6q   ��6(   �� *Settings.SteamPath3+6q   5e      ]� 5g   
   #��[ 6   $0
 *e.g C:/Program Files (x86)/Steam/steamapps��68   $��	30,0,0,10q�6�   $
��Left=�6�   $	��350��6�   $��21��6�   {�6m   �� $ enablesteam��$ 	IsChecked�.+�5h      �� $��Path 4:��6   $
��Left=�6'   $��15��6B   $	��Top=�6N   �� 5i      $��10,0,0,0q�6   $��20��6M   $	��Top=�6Y   $	��300��6q   ��6(   �� *Settings.SteamPath4+6q   5j      ]� 5l   
   #��[ 6   $0
 *e.g C:/Program Files (x86)/Steam/steamapps��68   $��	30,0,0,10q�6�   $
��Left=�6�   $	��350��6�   $��21��6�   {�6m   �� $ enablesteam��$ 	IsChecked�.+�5m      �� $��Path 5:��6   $
��Left=�6'   $��15��6B   $	��Top=�6N   �� 5n      $��10,0,0,0q�6   $��20��6M   $	��Top=�6Y   $	��300��6q   ��6(   �� *Settings.SteamPath5+6q   5o      �� 5u   
   -   5        $��0,0,0,0q�5u      	 6$   �� *Settings.EnableEpic+.��5v      �� $��Enable Epic Games support��6   5w      5y      5z      