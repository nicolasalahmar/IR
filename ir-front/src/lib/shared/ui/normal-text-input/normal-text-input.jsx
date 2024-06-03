//@Third Party
import { cn } from "@/shared/utils/tailwind-merge/tailwind-merge";

export function NormalTextInput({
  type,
  name,
  label,
  value,
  onChange,
  disabled,
  className,
  placeholder,
}) {
  return (
    <div className="group">
      <label className="flex flex-col gap-2">
        <span
          className={cn(
            "text-base font-normal text-black dark:text-white sm:text-sm",
            "group-focus-within:text-primary"
          )}
        >
          {label}
        </span>
        <div className={(cn(className), "relative")}>
          <input
            className={cn(
              // sizes
              "w-full h-full",

              // border
              "border border-gray rounded-lg dark:border-darkGray",

              // input
              "py-3 px-4 text-base text-black dark:bg-black dark:text-white sm:text-sm",

              // focus state
              "focus:outline-none focus:border focus:border-primary",

              // placeholder
              "placeholder:text-gray dark:placeholder:text-darkGray sm:placeholder:text-sm"
            )}
            name={name}
            placeholder={placeholder}
            disabled={disabled}
            type={type}
            value={value}
            onChange={(e) => onChange(e.target.value)}
          />
        </div>
      </label>
    </div>
  );
}
