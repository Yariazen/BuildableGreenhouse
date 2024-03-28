using StardewModdingAPI;
using StardewModdingAPI.Events;
using xTile;

namespace BuildableGreenhouse
{
    public class BuildableGreenhouse : Mod
    {
        public override void Entry(IModHelper helper)
        {
            helper.Events.Content.AssetRequested += this.OnAssetRequested;
        }

        private void OnAssetRequested(object? sender, AssetRequestedEventArgs e)
        {
            if (e.NameWithoutLocale.IsEquivalentTo("Maps\\GreenhouseMap"))
            {
                e.Edit(asset =>
                {
                    Map greenhouseIndoorMap = asset.AsMap().Data;
                    greenhouseIndoorMap.Properties["IsGreenhouse"] = true;
                });
            }
        }
    }
}
