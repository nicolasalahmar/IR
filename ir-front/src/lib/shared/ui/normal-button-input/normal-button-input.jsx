//@Dev
// # Shared
// ## UI
import { LoadingIndicator } from "..";
// ## Utils
import { cn } from "@/shared/utils/tailwind-merge/tailwind-merge";

export function NormalButtonInput({
  label,
  disabled,
  className,
  isLoading,
  onClick,
  type,
}) {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className={cn(
        // sizes
        "h-12 w-96",

        // colors
        "bg-primary text-white dark:bg-primary-light dark:text-black",

        // border
        "rounded-lg ",

        // content
        "font-semibold text-base flex items-center justify-center gap-3 sm:text-sm",

        // primary
        "cursor-pointer",

        //disabled
        "disabled:bg-primary/45 disabled:pointer-events-none",

        // pressed
        // "hover:bg-primary-dark",

        { "opacity-80 pointer-events-none": isLoading },

        {
          "border border-primary bg-white text-primary hover:bg-white-dark ":
            type === "outline",
        },

        //external style
        className
      )}
    >
      {isLoading && <LoadingIndicator className="w-[1.1rem] h-[1.1rem]" />}
      {label}
    </button>
  );
}
